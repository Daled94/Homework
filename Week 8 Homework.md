## Section 1 answers 

 SELECT rtrim(Accel,4) as 'AccelSec'
 FROM CleaningLab

 UPDATE CleaningLab
 SET Accel = RTRIM(Accel,' sec')

 ALTER TABLE CleaningLab
 RENAME Accel TO Accelsec
 SELECT Accelsec from CleaningLab

## SECTION 2 questions
### 2.1 - 2.5
SELECT Topspeed, Range, Efficiency, FastCharge
FROM CleaningLab
LIMIT 10

SELECT TopSpeed FROM CleaningLab
UPDATE CleaningLab
SET Topspeed = RTRIM(Topspeed, 'km/h');

SELECT Topspeed, RTRIM(Topspeed, 'hm/h')
FROM CleaningLab


### 2.6 
SELECT TopSpeed,ROUND(Topspeed * .621371, 2)
FROM CleaningLab

### 2.7
UPDATE CleaningLab
SET TopSpeed = TopSpeed * .621371

### 2.8
SELECT *
FROM CleaningLab

## SECTION 3 questions
### 3.1 & 3.2
SELECT Range, FROM CleaningLab
UPDATE CleaningLab
SET Range = RTRIM(range, 'km')

### 3.3
SELECT Range, RTRIM(range, 'km')
FROM CleaningLab

### 3.4
UPDATE CleaningLab
SET Range = RTRIM(Range, 'km')

### 3.5
-- SELECT *
-- FROM CleaningLab

### 3.6
 SELECT RANGE, ROUND(Range *0.621371, 1) AS RangeMiles
 FROM Cleaninglab

 UPDATE CleaningLab
SET Range = ROUND(Range * 0.621371, 1)

### 3.7
-- ALTER TABLE CleaningLab
-- RENAME COLUMN Range TO Rangemiles;

### 3.8
SELECT *
FROM Cleaninglab

## SECTION 4 questions
### 4.1
SELECT Efficiency, FastCharge
FROM CleaningLab

### 4.2 + 4.3
SELECT RTRIM(Efficiency, ' Wh/km'),  RTRIM(FastCharge, ' km/h')
FROM CleaningLab;

### 4.4
UPDATE CleaningLab
SET Efficiency = RTRIM(Efficiency, ' Wh/km')
    fastcharge = RTRIM(fastcharge, ' km/h')

### 4.5
SELECT *
FROM CleaningLab

### 4.6
-- SELECT FastCharge,
--   ROUND(FastCharge * 0.621371, 1) AS OneHourFastChargeMiles
-- FROM CleaningLab

-- UPDATE CleaningLab
-- SET FastCharge =ROUND(FastCharge* 0.621371)

### 4.7
ALTER TABLE CleaningLab
RENAME COLUMN FastCharge TO OneHourFastChargeMiles;

ALTER TABLE CleaningLab
RENAME COLUMN Efficiency TO EfficiencyWHperKM;

### 4.8
SELECT *
FROM CleaningLab

## SECTION 5 questions
### 5.1
SELECT RapidCharge, COUNT(*) 
FROM CleaningLab
GROUP BY RapidCharge

### 5.2
UPDATE CleaningLab
SET RapidCharge = 'Yes'
WHERE RapidCharge = 'Rapid charging possible';

UPDATE CleaningLab
SET RapidCharge = 'No'
WHERE RapidCharge = 'Rapid charging not possible'; 

### 5.3
Rapid charging possible = Yes
Rapid charging not possible = No


## SECTION 6 questions
### 6.1
Select Powertrain, COUNT(*)
FROM CleaningLab

### 6.2
- If the PowerTrain equals All Wheel Drive then I want you to change the value to 'AWD'
- If the PowerTrain equals Rear Wheel Drive then I want you to change the value to 'RWD'
- If the PowerTrain equals Forward Wheel Drive then I want you to change the value to 'FWD'

### 6.3
UPDATE CleaningLab
SET PowerTrain = 'AWD'
WHERE PowerTrain = 'All Wheel Drive';

UPDATE CleaningLab
SET PowerTrain = 'RWD'
WHERE PowerTrain = 'Rear Wheel Drive';

UPDATE Cleaninglab  
SET PowerTrain = 'FWD'
WHERE PowerTrain = 'Forward Wheel Drive';

### 6.4
SELECT *   
FROM CleaningLab


## SECTION 7 questions
### 7.1
SELECT priceEuro, ROUND(priceEuro * 1.09, 2)
FROM Cleaninglab

### 7.2
UPDATE CleaningLab
SET priceEuro = ROUND(priceEuro * 1.09, 2)

SELECT priceEuro
FROM evCars

### 7.3
ALTER TABLE CleaningLab
RENAME PriceEuro TO PriceUSD






