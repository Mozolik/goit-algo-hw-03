from datetime import datetime

def get_days_from_today(date):
    try:
        data_type = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        return 0
    
    data_today = datetime.today()
    count_days = (data_type - data_today).days
    return count_days

