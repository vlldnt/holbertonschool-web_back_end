-- SQL Script that create a stored procedure the store average score for student
DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser (
    IN user_id INT
)

BEGIN
    UPDATE users
        SET average_score = (
            SELECT AVG(score)
            FROM corrections
            WHERE user_id = users.id
        )
    WHERE id = user_id;

END$$

DELIMITER;