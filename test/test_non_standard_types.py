# -*- coding: UTF-8 -*-

import pytest
from sqlalchemy.testing import fixtures, config
from sqlalchemy import MetaData, Table, Column, Integer



class NonStandardTypesTest(fixtures.TablesTest):
    __backend__ = True

    @classmethod
    def define_tables(cls, metadata):
        cls.schema = "NonStandardTypesTest".upper()
        with config.db.begin() as c:
            try:
                c.execute("DROP SCHEMA %s CASCADE" % cls.schema)
            except Exception as e:
                print(e)
                pass
            c.execute("CREATE SCHEMA %s" % cls.schema)

    def test_hash_type(self):
        try:
            with config.db.begin() as c:
                c.execute(
                    """
                    CREATE OR REPLACE TABLE %s.table_hash (
                        col_hash HASHTYPE 
                        )
                    """ % self.schema)
                c.execute("commit")
            meta = MetaData(bind=config.db, schema=self.schema)
            meta.reflect()
            print("BBBBB", meta.tables)
            for i in meta.tables:
                print("AAAAAAA",i)
            pytest.fail()
        finally:
            with config.db.begin() as c:
                c.execute(
                    """
                    DROP TABLE IF EXISTS %s.table_hash;
                    """ % self.schema)
                c.execute("commit")

    def test_geometry(self):
        try:
            with config.db.begin() as c:
                c.execute(
                    """
                    CREATE OR REPLACE TABLE %s.table_geometry (
                        col_geometry GEOMETRY
                        )
                    """ % self.schema)
                c.execute("commit")
            meta = MetaData(bind=config.db, schema=self.schema)
            meta.reflect()
            print("BBBBB", meta.tables)
            for i in meta.tables:
                print("AAAAAAA",i)
            pytest.fail()
        finally:
            with config.db.begin() as c:
                c.execute(
                    """
                    DROP TABLE IF EXISTS %s.table_geometry;
                    """ % self.schema)
                c.execute("commit")

    def test_interval_year_month(self):
        try:
            with config.db.begin() as c:
                c.execute(
                    """
                    CREATE OR REPLACE TABLE %s.table_interval_year_month (
                        col_interval_year_month INTERVAL YEAR TO MONTH
                        )
                    """ % self.schema)
                c.execute("commit")
            meta = MetaData(bind=config.db, schema=self.schema)
            meta.reflect()
            print("BBBBB", meta.tables)
            for i in meta.tables:
                print("AAAAAAA",i)
            pytest.fail()
        finally:
            with config.db.begin() as c:
                c.execute(
                    """
                    DROP TABLE IF EXISTS %s.table_interval_year_month;
                    """ % self.schema)
                c.execute("commit")

    def test_interval_day_second(self):
        try:
            with config.db.begin() as c:
                c.execute(
                    """
                    CREATE OR REPLACE TABLE %s.table_interval_day_second (
                        col_interval_day_second INTERVAL DAY TO SECOND
                        )
                    """ % self.schema)
                c.execute("commit")
            meta = MetaData(bind=config.db, schema=self.schema)
            meta.reflect()
            print("BBBBB", meta.tables)
            for i in meta.tables:
                print("AAAAAAA",i)
            pytest.fail()
        finally:
            with config.db.begin() as c:
                c.execute(
                    """
                    DROP TABLE IF EXISTS %s.table_interval_day_second;
                    """ % self.schema)
                c.execute("commit")

