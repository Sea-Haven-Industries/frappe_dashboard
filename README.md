# Frappe Dashboard

A role-based landing page for link navigation

### Installation

You can install this app using the bench CLI:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app https://github.com/Sea-Haven-Industries/frappe_dashboard --branch main
bench --site {your-site-name} install-app dashboard
```

### Contributing

This app uses `pre-commit` for code formatting and linting. Please [install pre-commit](https://pre-commit.com/#installation) and enable it for this repository:

```bash
cd apps/dashboard
pre-commit install
```

Pre-commit is configured to use the following tools for checking and formatting your code:

- ruff
- eslint
- prettier
- pyupgrade

### License

mit