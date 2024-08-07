def evaluate_resume(resume_info, job_requirements):
    score = 0
    
    for skill in job_requirements.get("skills", []):
        if skill in resume_info.get("skills", []):
            score += 10
    
    for exp in job_requirements.get("experience", []):
        if exp in resume_info.get("experience", []):
            score += 15
    
    # Add more evaluation criteria as needed
    return score
