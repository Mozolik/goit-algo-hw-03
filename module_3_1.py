from datetime import datetime

def get_days_from_today(date):
    try:
        data_type = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        return None
    
    data_today = datetime.today()
    data_today = data_today.combine(data_today.date(), data_today.min.time())
    count_days = (data_type - data_today).days
    return count_days
