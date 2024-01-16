insert into company (name, bussiness, mvv, required_skill, location, benefit, applying_motivation) 
values ('A', NULL, NULL, NULL, NULL, NULL, NULL);

insert into company (name, bussiness, mvv, required_skill, location, benefit, applying_motivation) 
values ('B','bussiness B', 'mvv B', 'required_skill B', 'location B', 'benefit B', 'applying_motivation B');

-- insert into company (name, bussiness, mvv, required_skill, location, benefit, applying_motivation) 
-- values ('C','業務内容C', '経営理念C', '求められているスキルC', '勤務地C', '福利厚生C', '志望動機C');

insert into company_connection (company_id, company_date, way, employee, content, route) 
values (1, '2024-01-16', NULL, NULL, 'content A', NULL);

insert into company_connection (company_id, company_date, way, employee, content, route) 
values (2, '2024-01-01', 'way B', 'employee B', 'content B', 'route B');

-- insert into company_connection (company_id, company_date, way, employee, content, route) 
-- values (3, '2023-012-31', '接触方法C', '担当者C', '内容C', '経由C');