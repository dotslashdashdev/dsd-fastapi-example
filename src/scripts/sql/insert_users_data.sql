TRUNCATE TABLE users;
INSERT INTO users (id, email, status, nickname, join_datetime, leave_datetime) VALUES
('6c70712c-0aa1-4a2a-848d-f865bf94e36e', 'user1@dotslashdash.com', 'activation', 'user1', '2022-07-08T15:00:00+00:00', null),
('bc49695e-2e8a-45a0-ba74-bdec0f4b367f', 'user2@dotslashdash.com', 'deactivation', 'user2', '2022-07-08T16:30:00+00:00', '2022-09-23T06:20:00+00:00'),
('dd24e2fc-2492-44a2-b6a9-b831a9310ba0', 'user3@dotslashdash.com', 'activation', 'user3', '2022-10-01T05:23:00+00:00', null),
('b7fdfd98-ca1b-44ff-962d-4f5cbf4dbe8c', 'user4@dotslashdash.com', 'activation', 'user4', '2022-10-07T12:34:00+00:00', null),
('21969938-814b-4e9d-b209-61d307931c72', 'user5@dotslashdash.com', 'activation', 'user5', '2022-10-07T13:09:00+00:00', null),
('a14c2a97-626e-44bd-95cf-f9080a00bd98', 'user6@dotslashdash.com', 'activation', 'user6', '2022-10-08T06:42:00+00:00', null),
('61b21802-568c-4667-965e-32228854089d', 'user7@dotslashdash.com', 'activation', 'user7', '2022-10-09T09:01:00+00:00', null),
('ed13fb2f-33df-4a48-9cf3-5baca0a4b2fb', 'user8@dotslashdash.com', 'deactivation', 'user8', '2022-10-10T14:39:00+00:00', '2022-10-12T16:57:49+00:00'),
('94f68c04-8867-473e-959d-9fc996abad7e', 'user9@dotslashdash.com', 'activation', 'user9', '2022-10-11T11:23:00+00:00', null),
('7c2724bd-b8d5-40f4-948e-f20353c991a8', 'user10@dotslashdash.com', 'activation', 'user10', '2022-10-11T05:54:00+00:00', null);