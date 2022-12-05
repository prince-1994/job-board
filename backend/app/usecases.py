from app.repositories import CompanyRepository, JobRepository, UserRepository


class UserUsecases:
    def __init__(self, user_repo: UserRepository):
        self.repo = user_repo

class JobUsecases:
    def __init__(self, job_repo: JobRepository):
        self.repo = job_repo

class CompanyUsecases:
    def __init__(self, company_repo: CompanyRepository):
        self.repo = company_repo