import datetime

def deploy_app():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Simulating deployment at {timestamp}...")
    print("Application deployed successfully! ✅")

if __name__ == "__main__":
    deploy_app()
