# SurfersFlaskAccelerator
Web frontend scaffolding written in Python with the Flask micro framework for futher project modules aligned to the Surfers Lookout system. 

# Overview
Simple single page web service that will display a colored circle based on the configuration setting of the *COLOR* config setting. This can be set via the config module or via the *COLOR* environment variable (can be set in the .env file for testing).
e.g. **export COLOR=red** will display a red circle as root page


# Technical Detail
## Code Details
- Language: Python 3.10+
- Web Framework: [Flask](https://flask.palletsprojects.com) 
- Data access via [SqlAchemy](https://www.sqlalchemy.org/) 
- Functional and Unit testing with [Pytest](https://docs.pytest.org)

## Platform
- [Tanzu Application Platform](https://tanzu.vmware.com/application-platform) 1.3+

