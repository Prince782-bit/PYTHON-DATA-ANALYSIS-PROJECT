CREATE DATABASE mydata;
USE mydata;

CREATE TABLE hospital (

    Nameoftablets VARCHAR(100),
    ref VARCHAR(100) PRIMARY KEY,
    Dose VARCHAR(100),
    NumberofTablets VARCHAR(100),
    Lot VARCHAR(100),
    Issuedate VARCHAR(100),
    ExpDate VARCHAR(100),
    DailyDose VARCHAR(100),
    sideEfect VARCHAR(100),
    FurtherInformation VARCHAR(255),
    StorageAdvice VARCHAR(255),
    DrivingUsingMachine VARCHAR(100),
    HowToUseMedication VARCHAR(255),
    PatientId VARCHAR(100),
    nhsNumber VARCHAR(100),
    PatientName VARCHAR(100),
    DateOfBirth VARCHAR(100),
    PatientAddress VARCHAR(255)

);
select * from hospital;

