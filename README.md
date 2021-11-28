## Assignment 11: Mini-Project 4: Bank Service
### Group: Benjamin, Amanda and Amalie

### Tasks:
- [x] Create a model of the business process in BPMN.
- [x] Create a rule engine with the business rules, applied for validation of applications.
- [x] Create service task for adding details about the bank loan and creating a document out of it.
- [ ] Integrate and deploy the whole process on a web server.
- [x] Self invented alternative: Integrate and deploy the whole process on a local server.
- [x] Test the operability by sending application messages from either a REST client or a message broker.
- [x] Upload the code and the model files in your Github repository, add some screenshots of the models, and a brief readme file.

### Bank BPMN process:
![](https://github.com/kongshaug/Comunda_bank/blob/main/documentation_screenshots/model.PNG)


### Here we will take you through a successful process. 

First step is to create a loan application by entering client information:

![](https://github.com/kongshaug/Comunda_bank/blob/main/documentation_screenshots/step_1.PNG)

After the information is entered a automated bank liability system determains if the client should be offered a loan.
In this case the system determined that the client should be offered a loan.

![](https://github.com/kongshaug/Comunda_bank/blob/main/documentation_screenshots/step_2.PNG)

This decision was made on the basic of the information the client has entered about themself and determined by the code seen below.
Notice that the system said "second condition" this is because the interest rate and price of a loan depends on the amount the client wants to borrow and the personal information the client has given. The specific rules can be seen below.

If there is mistakes in the information the system has been given a bpmn error is thrown, the client is informed and the client has to start over.

![](https://github.com/kongshaug/Comunda_bank/blob/main/documentation_screenshots/step_3.PNG)

After the system has handled the request a employee looks over the information given by the client, the offer the system has offered the client. Here he/she has the option to change the price, interest rate or cancel the loan altogether. 

![](https://github.com/kongshaug/Comunda_bank/blob/main/documentation_screenshots/step_4.PNG)

When the employee has accepted the loan the client is presented with almost the same information except whether the system has deemed them liable because this is internal information for the bank only.

Here the client has the option to accept or decline the loan.
![](https://github.com/kongshaug/Comunda_bank/blob/main/documentation_screenshots/step_5.PNG)

If the client accepts the loan a record of the loan and all of the information about the client is saved:
![](https://github.com/kongshaug/Comunda_bank/blob/main/documentation_screenshots/step_6.PNG)


