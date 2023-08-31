from django.db import connection


def add_default_constraint():
    with connection.cursor() as cursor:
        cursor.execute(
            """
            USE [ins_db]
            GO
            ALTER TABLE [dbo].[environment_diction]
            ADD CONSTRAINT [DF_environment_diction_created_at]
            DEFAULT (getdate()) FOR [created_at]
            """
        )
        cursor.execute(
            """
            USE [ins_db]
            GO 
            ALTER TABLE 
            [dbo].[environment_instypes] 
            ADD  CONSTRAINT [DF_environment_instypes_created_at]  
            DEFAULT (getdate()) FOR [created_at]
            """
        )
