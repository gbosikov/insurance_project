USE [ins_db]
GO


ALTER TABLE [dbo].[environment_diction]
            ADD CONSTRAINT [DF_environment_diction_created_at]
            DEFAULT (getdate()) FOR [created_at]

ALTER TABLE
            [dbo].[environment_instypes]
            ADD  CONSTRAINT [DF_environment_instypes_created_at]
            DEFAULT (getdate()) FOR [created_at]


ALTER TABLE
            [dbo].[environment_risks]
            ADD  CONSTRAINT [DF_environment_risks_created_at]
            DEFAULT (getdate()) FOR [created_at]

ALTER TABLE
            [dbo].[environment_objects]
            ADD  CONSTRAINT [DF_environment_robjects_created_at]
            DEFAULT (getdate()) FOR [created_at]

INSERT INTO [dbo].[environment_diction]
           ([custom_name]
           ,[name_e]
           ,[name_g]
           ,[name_r]
           ,[custom_order]
           ,[color]
           ,[visible]
           ,[created_at]
		   ,[user_id])
     VALUES
           ('car_mark',
           'car mark',
           N'მანქანის მარკა',
           N'марка авто',
           0,
           '0',
           1,
           GETDATE(),
		   1)



INSERT INTO [dbo].[environment_instypes]
           ([custom_name]
           ,[name_e]
           ,[name_g]
           ,[name_r]
           ,[created_at]
           ,[diction_id]
		   ,[user_id])
     VALUES
           ('5.1',
           'casco',
           N'ავტოტრანსპორტის დაზღვევა (ავტოკასკო)',
           N'Автокаско',
           GETDATE(),
           1,
		   1)
GO


