# AWS Build Test

This is a simple Python application that will be used to test the AWS CodeBuild service.

## Files

- `myApp.py`: The main application file.
- `test.py`: The test file.
- `buildspec.yml`: The buildspec file.
- `README.md`: The readme file.
- `.gitignore`: The gitignore file.

## Usage

```bash
python myApp.py
```

## Testing

```bash
python -m unittest test.py
```

## Buildspec

The buildspec file is used to define the build process.

```yaml
version: 0.2

phases:
  install:
    runtime-versions:
      python: 3.10
  build:
    commands:
      - echo "Running tests..."
      - python -m unittest test.py
  post_build:
    commands:
      - echo "Build completed successfully"

artifacts:
  files:
    - myApp.py
    - test.py
    - buildspec.yml
    - README.md
    - .gitignore
