## 7.1 HW Questions
## Question 1
-- SELECT ModelYear, Make, Model
FROM evRegistry

## Question 2
-- SELECT DISTINCT ElectricVehicleType
FROM evRegistry;

## Question 3
-- SELECT *
FROM evRegistry
WHERE ElectricVehicleType = 'BEV';

## Question 4
-- SELECT Make, Model
FROM evRegistry
WHERE BaseMSRP BETWEEN 20000 AND 35000;

## 7.2 HW Questions
## Question 1
SELECT *
FROM evRegistry
WHERE City IS NULL;

## Question 2
SELECT Make, Model, ElectricVehicleType
FROM evRegistry
WHERE VIN LIKE '%3E1EA1J';

## Question 3
SELECT ModelYear, Make, Model, ElectricVehicleType, ElectricRange
FROM evRegistry
WHERE Make IN ('Tesla', 'Chevrolet')
ORDER BY Make, ModelYear DESC;

## Question 4
SELECT stationId, COUNT(*) AS NumUsages
FROM evCharge
GROUP BY stationId
ORDER BY NumUsages DESC
LIMIT 5;

## Question 5
SELECT userId, MIN(chargeTimeHrs) AS minTime, MAX(chargeTimeHrs) AS maxTime
FROM evCharge
WHERE chargeTimeHrs > 0.5
GROUP BY userId
ORDER BY minTime, maxTime;

## 7.3 HW Questions
## Question 1
SELECT weekday, AVG(chargeTimeHrs) AS 'AverageChargingTime'
FROM EVCharging
GROUP BY weekday
ORDER BY 'AverageChargingTime' DESC
LIMIT 1;

## Question 2
SELECT userid,ROUND(SUM(kwhTotal),2) AS 'totalPower'
FROM EVCharging
GROUP BY userid
ORDER BY 'totalPower' DESC
LIMIT 15;


## Question 3
SELECT typeFacility, COUNT(*) AS 'numStation'
FROM dimFacility
INNER JOIN factCharge ON dimFacility.typeFacility
GROUP BY typeFacility
ORDER BY 'numStation' DESC

## Question 4
Primary keys are unique identifiers for each row in a table. Foreign keys are used to link tables together. They are a column in one table that references the primary key of another table, forign keys can be used to create relationships between tables.

## Question 5
SELECT userid, MIN(chargeTimeHrs) AS minTime, MAX(chargeTimeHrs) AS maxTime
FROM EVCharging
WHERE chargeTimeHrs > 1
GROUP BY userid
HAVING minTime != maxTime

