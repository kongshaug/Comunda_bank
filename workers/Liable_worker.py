from camunda.external_task.external_task import ExternalTask, TaskResult
from camunda.external_task.external_task_worker import ExternalTaskWorker
import threading

# configuration for the Client
default_config = {
    "maxTasks": 1,
    "lockDuration": 10000,
    "asyncResponseTimeout": 5000,
    "retries": 3,
    "retryTimeout": 5000,
    "sleepSeconds": 30}


def liability(task: ExternalTask) -> TaskResult:
    """
    This task handler you need to implement with your business logic.
    After completion of business logic call either task.complete() or task.failure() or task.bpmn_error() 
    to report status of task to Camunda
    """
    print("Determening liability of new client...")

    Age = task.get_variable("Age")
    Name = task.get_variable("Name")
    Salary = task.get_variable("Salary")
    Amount = task.get_variable("Amount")
    Address = task.get_variable("Address")
    Married = task.get_variable("Married")
    Have_loan = task.get_variable("Have_loan")

    print(Age, Name, Salary, Amount, Address, Married, Have_loan)
    Liable, Price, Interest = False, 0, 0.0
    bpmn_error = False

    if Amount == 0 or Salary == 0 or Age < 12:
        bpmn_error = True

    elif Amount < 10000 and Have_loan == None:
        print("Loan Accepted... first condition")
        Liable, Price, Interest = True, 100, 4.2
    elif Amount < 50000 and Have_loan == None and Salary > 30000 and Age > 18:
        print("Loan Accepted... second condition")
        Liable, Price, Interest = True, 2000, 3.0
    elif Amount < 100000 and Have_loan == None and Salary > 40000 and Married != None and Age > 28:
        print("Loan Accepted... third condition")
        Liable, Price, Interest = True, 30000, 1.0
    elif Amount >= 100000 and Have_loan == None and Salary > 45000 and Married != None and Address != None and Age > 35:
        print("Loan Accepted... forth condition")
        Liable, Price, Interest = True, 6000, 0.5

    if bpmn_error:
        return task.bpmn_error(error_code="Client_information_error", error_message="Client data error.. try restarting the process")

    print("The customers liable status was: ", Liable)
    return task.complete({
        "Age": Age, "Name": Name, "Salary": Salary, "Amount": Amount, "Address": Address, "Married": Married, "Have_loan": Have_loan, "Liable": str(Liable), "Price": Price, "Interest": Interest
    })


def saving_loan(task: ExternalTask) -> TaskResult:
    print("Saving client information...")

    Age = task.get_variable("Age")
    Name = task.get_variable("Name")
    Salary = task.get_variable("Salary")
    Amount = task.get_variable("Amount")
    Address = task.get_variable("Address")
    Married = task.get_variable("Married")
    Liable = task.get_variable("Liable")
    Price = task.get_variable("Price")
    Interest = task.get_variable("Interest")
    Have_loan = task.get_variable("Have_loan")

    print("saving new loan...")
    loan = """
    {} age: {} has a loan of {}. with a interest of {}%. The price is {}. He/She Has a salary of {}. Lives at: {}. Marriage status {}. 
    """.format(Name, Age, Amount, Interest, Price, Salary, Address, Married)

    with open('../loans/loan_records.txt', 'a') as records:
        records.write('{}\n'.format(loan))

    return task.complete({
        "Age": Age, "Name": Name, "Salary": Salary, "Amount": Amount, "Address": Address, "Married": Married, "Have_loan": Have_loan, "Liable": str(Liable), "Price": Price, "Interest": Interest
    })


def handle_liability():
    ExternalTaskWorker(worker_id="1", config=default_config).subscribe(
        "Liable", liability)


def handle_saving_loan():
    ExternalTaskWorker(worker_id="2", config=default_config).subscribe(
        "Loan_accepted", saving_loan)


if __name__ == '__main__':
    print("Starting Handelers...")
    t1 = threading.Thread(target=handle_liability)
    t1.start()
    t2 = threading.Thread(target=handle_saving_loan)
    t2.start()
    print("Handelers started...")
