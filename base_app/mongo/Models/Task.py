class Task:
    def __init__(self, company_id, team_id, parental_task_id, task_info, startdate, deadline, enddate, priority,
                 difficulty, sub_tasks, status, ancestor_task_id, task_id=None):
        if task_id is None:
            self.task_id = -1
        else:
            self.task_id = task_id
        self.company_id = company_id
        self.team_id = team_id
        self.parental_task_id = parental_task_id
        self.task_info = task_info
        self.start_date = startdate
        self.deadline = deadline
        self.end_date = enddate
        self.priority = priority
        self.difficulty = difficulty
        self.sub_tasks = sub_tasks
        self.status = status
        self.ancestor_task_id = ancestor_task_id

    def get_task_id(self):
        return self.task_id

    def set_task_id(self, task_id):
        self.task_id = task_id

    def get_company_id(self):
        return self.company_id

    def set_company_id(self, company_id):
        self.company_id = company_id

    def get_team_id(self):
        return self.team_id

    def set_team_id(self, team_id):
        self.team_id = team_id

    def get_parental_task_id(self):
        return self.parental_task_id

    def get_task_info(self):
        return self.task_info

    def get_start_date(self):
        return self.start_date

    def get_deadline(self):
        return self.deadline

    def get_end_date(self):
        return self.end_date

    def set_end_date(self, end_date):
        self.end_date = end_date

    def get_priority(self):
        return self.priority

    def get_difficulty(self):
        return self.difficulty

    def get_sub_tasks(self):
        return self.sub_tasks

    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = status

    def get_ancestor_task_id(self):
        return self.ancestor_task_id