from collections import Counter

logs = [
    {"user": "Test1", "action": "login", "status": "success"},
    {"user": "Test2", "action": "login", "status": "fail"},
    {"user": "Test1", "action": "upload", "status": "success"},
    {"user": "Test3", "action": "login", "status": "success"},
    # {"user": "Test1", "action": "upload", "status": "success"},
    {"user": "Test3", "action": "download", "status": "fail"},
]


# Log analysis functions
# To count the number of successful logs
def count_success_logs(logs):
    count = sum(1 for log in logs if log["status"] == "success")
    return count


# To count the number of failed login attempts
def failed_login_count(logs):
    count = sum(
        1 for log in logs if log["status"] == "fail" and log["action"] == "login"
    )
    return count


# To count the total number of failed logs
def total_failed_logs(logs):
    count = sum(1 for log in logs if log["status"] == "fail")
    return count


# To count the number of activities performed by each user
def user_activity_count(logs):
    user_activity = Counter(log["user"] for log in logs)
    return user_activity


# To identify the most active user based on the number of activities performed
def most_active_user(logs):
    # return max(user_activity_summary().items(), key=lambda x: x[1])  -- wroks for returning single user but if there is a draw
    data = user_activity_count(logs)
    max_count = max(data.values())  # comparing values in key-value
    winners = [user for user, count in data.items() if count == max_count]
    return winners


if __name__ == "__main__":
    print(f"Success log count: {count_success_logs(logs)}")
    print(f"Failed log count: {total_failed_logs(logs)}")
    print(f"Failed login count: {failed_login_count(logs)}")
    print(f"User activity count summary:{user_activity_count(logs)}")
    print(f"Most active user:{most_active_user(logs)}")
