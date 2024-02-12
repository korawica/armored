# Changelogs

## Latest Changes

## 0.0.3

### Features

- :dart: feat: add file model for json and parquet. (_2024-02-02_)
- :dart: feat: add Connection model for support url connection string. (_2024-02-02_)

### Code Changes

- :construction: refactored: create folder for datasets that contain file and db. (_2024-02-02_)
- :construction: refactored: ⬆ bump actions/cache from 3 to 4 (_2024-02-01_)
- :construction: refactored: move Col and Tbl from catalogs to dataset. (_2024-02-01_)
- :construction: refactored: change folder name for abbrevation. (_2024-02-01_)

### Documents

- :page_facing_up: docs: update API docs for list all models on data types. (_2024-02-12_)

### Build & Workflow

- :toolbox: build: add ci workflow for upload coverage report. (_2024-02-12_)

## 0.0.2

### Features

- :dart: feat: add Msg and Stm model for message and statement query. (_2024-01-30_)
- :dart: feat: add TS model for time data. (_2024-01-30_)
- :dart: feat: add from __future__ to all files and licensed comment. (_2024-01-30_)

### Code Changes

- :construction: refactored: change name of const from data to property. (_2024-01-31_)
- :test_tube: test: add example test case for pass data from yaml. (_2024-01-30_)
- :construction: refactored: change name of primary key model from PK to Pk. (_2024-01-30_)
- :test_tube: test: change timezone of testing tag and time model. (_2024-01-30_)
- :construction: refactored: change model name of PrimaryKey and ForeignKey to PK and FK. (_2024-01-30_)
- :construction: refactored: change model name of Column and Table to Col and Tbl. (_2024-01-30_)
- :construction: refactored: 🚧 [pre-commit.ci] auto fixes from pre-commit.com hooks (_2024-01-29_)

### Documents

- :page_facing_up: docs: add API docs for all features of this project. (_2024-01-31_)
- :page_facing_up: docs: update README for more information of project objective. (_2024-01-30_)
- :page_facing_up: docs: update sizing and pypi tracking to README. (_2024-01-14_)

### Fix Bugs

- :gear: fixed: revert of change version of actions/cache. (_2024-01-30_)
- :gear: fixed: change datetime now to utcnow. (_2024-01-30_)
- :gear: fixed: remove import future on all files. (_2024-01-30_)

### Build & Workflow

- :toolbox: build: update action cache version from 3 to 4. (_2024-01-30_)
- :toolbox: build: update deps of pydantic version to 2.6.0. (_2024-01-30_)

## 0.0.1

### Features

- :dart: feat: add enums for status in task model. (_2024-01-14_)
- :dart: feat: add BaseTable and Table models. (_2024-01-14_)
- :dart: feat: add extract_column_from_dtype method that prepare dtype string. (_2024-01-14_)
- :dart: feat: add column model that combine constraint and dtype together. (_2024-01-13_)

### Documents

- :page_facing_up: docs: update README and add extract dtype from string. (_2024-01-13_)
- :page_facing_up: docs: update description and shelf config on pyproject. (_2024-01-13_)

### Build & Workflow

- :toolbox: build: create dependabot.yml (_2024-01-11_)
