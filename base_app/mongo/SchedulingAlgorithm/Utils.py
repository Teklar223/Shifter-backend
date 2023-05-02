def get_maximal_workers(shift_template, date, starthour, endhour, role_id):
    if shift_template.get(date) is not None:
        for shift in shift_template[date]:
            if shift["StartHour"] == starthour and shift["EndHour"] == endhour and shift["RoleID"] == role_id:
                return shift["Workers"]
    return None


# TODO: create a function that change all answers to true