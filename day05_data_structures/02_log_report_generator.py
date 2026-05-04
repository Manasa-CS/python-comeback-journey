import log_data_analyzer as log_func
from collections import Counter

logs = [
    {"user": "Test1", "action": "login", "status": "success"},
    {"user": "Test2", "action": "login", "status": "fail"},
    {"user": "Test1", "action": "upload", "status": "success"},
    {"user": "Test3", "action": "login", "status": "success"},
    {"user": "Test1", "action": "upload", "status": "success"},
    {"user": "Test3", "action": "download", "status": "fail"},
    {"user": "Test3", "action": "upload", "status": "fail"},
    {"user": "Test4", "action": "login", "status": "fail"},
]


# Log report generation functions
# To generate a summary report of the logs, including total logs, success logs, failed logs, and unique users
def generate_summary_report(logs):
    success_log_count = log_func.count_success_logs(logs)
    failed_log_count = log_func.total_failed_logs(logs)
    total_log_count = len(logs)
    unique_user_count = len(log_func.user_activity_count(logs))
    report = {
        "total_logs": total_log_count,
        "success_logs": success_log_count,
        "failed_logs": failed_log_count,
        "unique_users": unique_user_count,
    }
    return report


# To identify users with multiple failed action attempts (potentially suspicious activity)
def suspicious_users(logs):
    user_failed_activity = Counter(
        log["user"] for log in logs if log["status"] == "fail"
    )
    return [user for user, count in user_failed_activity.items() if count >= 2]


# To identify the most common failed action in the logs
def most_failed_action(logs):
    failed_activity = Counter(log["action"] for log in logs if log["status"] == "fail")
    max_failed_count = max(failed_activity.values())
    return [
        action for action, count in failed_activity.items() if count == max_failed_count
    ]


# To print a formatted dashboard report summarizing the log analysis results
def print_dashboard(logs):
    summary = generate_summary_report(logs)
    print("=============LOG REPORT=============")
    print(f"Total Logs\t\t:{summary['total_logs']}")
    print(f"Success Logs\t\t:{summary['success_logs']}")
    print(f"Failed Logs\t\t:{summary['failed_logs']}")
    print(f"Unique Users\t\t:{summary['unique_users']}")
    print(f"Suspicious Users \t: {suspicious_users(logs)}")
    print(f"Most Failed Action\t: {most_failed_action(logs)} ")
    print("====================================")


if __name__ == "__main__":
    print(generate_summary_report(logs))
    print(suspicious_users(logs))
    print(most_failed_action(logs))
    print_dashboard(logs)
