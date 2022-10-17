CREATE TABLE `Metals`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `metal` NVARCHAR(160) NOT NULL,
    `price` NUMERIC(10,2) NOT NULL
);

CREATE TABLE `Sizes` 
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `carets` NUMERIC(4,2) NOT NULL,
    `price` NUMERIC(7, 2) NOT NULL
);

CREATE TABLE `Styles`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
    `style` NVARCHAR(20) NOT NULL, 
    `price` NUMERIC(6,2) NOT NULL
);

CREATE TABLE `Orders`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `metal_id` INTEGER NOT NULL,
    `size_id` INTEGER NOT NULL, 
    `style_id` INTEGER NOT NULL, 
    `timestamp` INTEGER NOT NULL,
    FOREIGN KEY (`metal_id`) REFERENCES `Metals` (`id`),
    FOREIGN KEY (`size_id`) REFERENCES `Sizes` (`id`),
    FOREIGN KEY (`style_id`) REFERENCES `Styles` (`id`)
);


INSERT INTO `Metals` VALUES (null, "Sterling Silver", 12.42);
INSERT INTO `Metals` VALUES (null, "14K Gold", 736.40);
INSERT INTO `Metals` VALUES (null, "24K Gold", 1258.90);
INSERT INTO `Metals` VALUES (null, "Platinum", 795.45);
INSERT INTO `Metals` VALUES (null, "Palladium", 1241.00);


INSERT INTO `Sizes` VALUES (null, 0.5, 405.00);
INSERT INTO `Sizes` VALUES (null, 0.75, 782.00);
INSERT INTO `Sizes` VALUES (null, 1, 1470.00);
INSERT INTO `Sizes` VALUES (null, 1.5, 1997.00);
INSERT INTO `Sizes` VALUES (null, 2, 3638.00);

INSERT INTO `Styles` VALUES (null, "Classic", 500.00);
INSERT INTO `Styles` VALUES (null, "Modern", 710.00);
INSERT INTO `Styles` VALUES (null, "Vintage", 965.00);

INSERT INTO `Orders` VALUES (null, 3, 2, 3, 1614659931693);
INSERT INTO `Orders` VALUES (null, 2, 2, 2, 1614659931694);
INSERT INTO `Orders` VALUES (null, 1, 5, 1, 1614659931695);
INSERT INTO `Orders` VALUES (null, 4, 3, 1, 1614659931696);
INSERT INTO `Orders` VALUES (null, 5, 4, 3, 1614659931697);


SELECT 
    o.*,
    m.*,
    si.*,
    st.*
FROM Orders o 
JOIN Metals m ON m.id = o.metal_id
JOIN Sizes si ON si.id = o.size_id
JOIN Styles st ON st.id = o.style_id
WHERE o.id = 1;






