USE [ins_db]
GO


ALTER TABLE [dbo].[diction]
            ADD CONSTRAINT [DF_environment_diction_created_at]
            DEFAULT (getdate()) FOR [created_at]

ALTER TABLE
            [dbo].[ins_types]
            ADD  CONSTRAINT [DF_environment_instypes_created_at]
            DEFAULT (getdate()) FOR [created_at]


ALTER TABLE
            [dbo].[risks]
            ADD  CONSTRAINT [DF_environment_risks_created_at]
            DEFAULT (getdate()) FOR [created_at]

ALTER TABLE
            [dbo].[objects]
            ADD  CONSTRAINT [DF_environment_robjects_created_at]
            DEFAULT (getdate()) FOR [created_at]

INSERT INTO [dbo].[diction]
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



INSERT INTO [dbo].[ins_types]
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


