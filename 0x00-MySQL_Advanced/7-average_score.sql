-- SQL script that creates a stored procedure ComputeAverageScoreForUser,
-- that computes and store the average score for a student,
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id int)
BEGIN
	DECLARE student_avg FLOAT;
	SELECT AVG(score) INTO student_avg FROM corrections
	WHERE corrections.user_id = user_id;

	UPDATE users
	SET average_score = student_avg
	WHERE id = user_id;
END $$
DELIMITER ;
