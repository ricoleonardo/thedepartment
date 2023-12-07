CREATE TABLE `employees` (
  `id` integer PRIMARY KEY,
  `name` varchar(255),
  `department_id` integer,
  `is_rover` boolean
);

CREATE TABLE `departments` (
  `id` integer PRIMARY KEY,
  `name` varchar(255),
  `head_id` integer
);

CREATE TABLE `divisions` (
  `id` integer PRIMARY KEY,
  `name` varchar(255)
);

CREATE TABLE `projects` (
  `id` integer PRIMARY KEY,
  `name` varchar(255),
  `description` text
);

CREATE TABLE `employee_projects` (
  `employee_id` integer,
  `project_id` integer
);

CREATE TABLE `department_members` (
  `id` integer,
  `department_id` integer,
  `employee_id` integer
);

ALTER TABLE `divisions` ADD FOREIGN KEY (`id`) REFERENCES `employees` (`id`);

ALTER TABLE `employees` ADD FOREIGN KEY (`department_id`) REFERENCES `divisions` (`name`);

ALTER TABLE `divisions` ADD FOREIGN KEY (`name`) REFERENCES `departments` (`name`);

ALTER TABLE `employee_projects` ADD FOREIGN KEY (`employee_id`) REFERENCES `employees` (`id`);

ALTER TABLE `employee_projects` ADD FOREIGN KEY (`project_id`) REFERENCES `projects` (`id`);

ALTER TABLE `departments` ADD FOREIGN KEY (`head_id`) REFERENCES `employees` (`id`);

ALTER TABLE `department_members` ADD FOREIGN KEY (`id`) REFERENCES `departments` (`id`);

ALTER TABLE `department_members` ADD FOREIGN KEY (`employee_id`) REFERENCES `employees` (`id`);
