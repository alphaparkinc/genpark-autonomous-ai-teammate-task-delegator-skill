from client import AutonomousAiTeammateTaskDelegatorClient

def main():
    client = AutonomousAiTeammateTaskDelegatorClient()
    res = client.delegate_task("Analyze competitor pricing tables for Q3 2026", "Market_Intelligence_Agent")
    print(f"Ticket ID: {res['task_ticket_id']}")
    print(f"Status: {res['delegation_status']}")
    print(f"Est Completion: {res['estimated_completion_min']} mins")

if __name__ == "__main__":
    main()
