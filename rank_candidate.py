from multiprocessing import cpu_count, Pool
from typing import Set
from pyresparser.utils import extract_skills
import pandas as pd
import spacy


def get_candidate_score(
        job_skill_count: int,
        job_skills: Set[str],
        candidate_skills: Set[str]
) -> float:
    """
    This function compares the candidate skills with job description skills
    and rates the candidate based on the fraction of common skills
    
    :param job_skill_count: Number of job skills
    :param job_skills: Set of job skills
    :param candidate_skills: Set of candidate skills
    :return: Candidate score
    """

    common_skills = job_skills.intersection(candidate_skills)
    candidate_score = float(len(common_skills)) / job_skill_count
    return candidate_score * 100


def get_candidate_score_wrapper(args: tuple) -> float:
    """
    A wrapper function to de-structure the tuple of arguments
    for multiprocessing.Pool.map()
    
    :param args: Tuple of arguments for the wrapped function
    :return: Result of the wrapped function
    """
    return get_candidate_score(*args)


def sort_candidates(
        job_desc_text: str,
        candidates_df: pd.DataFrame
) -> pd.DataFrame:
    """
    This function compares the skills of a number of candidates
    against the skills required of a given job description
    
    :param job_desc_text: Job description text
    :param candidates_df: DataFrame containing candidate details and skills
    :return: DataFrame with candidates sorted as per their match
     with the given job description
    """

    # Get the list of required skills from the Job description
    # and convert them to a set
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(job_desc_text)
    job_skills = set([
        skill.lower() for skill in extract_skills(doc, doc.noun_chunks)
    ])
    job_skill_count = len(job_skills)

    # Get the candidate skills from the dataframe and create
    # a set of skills for each candidate
    candidates_skills = candidates_df["Skills"].values.tolist()
    candidates_skills = [
        set([
            skill.strip().lower() for skill in skill_list.split(",")
        ])
        for skill_list in candidates_skills
    ]

    # Use multiprocessing to evaluate multiple candidates for
    # a given job in parallel
    num_executors = cpu_count()
    processing_data = [
        (job_skill_count, job_skills, person_skills)
        for person_skills in candidates_skills
    ]
    with Pool(num_executors) as process_pool:
        candidates_df["Score"] = process_pool.map(get_candidate_score_wrapper, processing_data)

    return candidates_df


if __name__ == '__main__':
    # Read candidate details
    df = pd.read_csv("resumes.csv", usecols=["Email", "Skills"])

    try:
        with open("sample_job_description.txt", "r") as fp:
            job_description = fp.read()
    except FileNotFoundError:
        job_description = None

    if job_description:
        ranked_df = sort_candidates(job_description, df)
        # Sort candidates in descending order of score
        ranked_df.sort_values(by="Score", ascending=False, inplace=True)
        ranked_df.to_csv("ranked.csv", index=False)
