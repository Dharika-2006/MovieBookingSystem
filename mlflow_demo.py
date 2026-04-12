import mlflow

print("Starting Movie Booking MLflow...")

mlflow.set_experiment("movie_booking_system")
with mlflow.start_run():

    mlflow.log_param("movie", "Avengers")
    mlflow.log_param("slot", "6PM")
    mlflow.log_param("tickets", 2)

    mlflow.log_metric("total_amount", 300)
    mlflow.log_metric("booking_success", 1)

    with open("ticket.txt", "w") as f:
        f.write("Movie: Avengers\nSlot: 6PM\nTickets: 2\nTotal: 300")

    mlflow.log_artifact("ticket.txt")

    print("Movie booking logged!")

print("Done!")