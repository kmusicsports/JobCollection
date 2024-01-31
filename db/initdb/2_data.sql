INSERT INTO
  company (name, business, mvv, required_skill, location, benefit, applying_motivation)
VALUES
  ('株式会社A', NULL, NULL, NULL, NULL, NULL, NULL),
  ('B株式会社','business B', 'mvv B', 'required_skill B', 'location B', 'benefit B', 'applying_motivation B'),
  ('（株）C','業務内容C', '経営理念C', '求められているスキルC', '勤務地C', '福利厚生C', '志望動機C');

INSERT INTO
  company_connection (company_id, connection_date, way, employee, content, route)
VALUES
  (1, '2024-01-16', NULL, NULL, 'content A', NULL),
  (2, '2024-01-01', 'way B', 'employee B', 'content B', 'route B'),
  (3, '2023-012-31', '接触方法C', '担当者C', '内容C', '経由C');
