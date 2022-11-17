CREATE TABLE IF NOT EXISTS `users` (
    `id` CHAR(36) NOT NULL  PRIMARY KEY COMMENT '사용자 고유 식별키',
    `email` VARCHAR(100)   COMMENT '이메일',
    `status` VARCHAR(12) NOT NULL  COMMENT '계정 상태' DEFAULT 'activation',
    `nickname` VARCHAR(50) NOT NULL  COMMENT '닉네임',
    `join_datetime` DATETIME(6) NOT NULL  COMMENT '가입 일시' DEFAULT CURRENT_TIMESTAMP(6),
    `leave_datetime` DATETIME(6)   COMMENT '탈퇴 일시'
);