# Good First Issues - Streamlit

A Streamlit-based frontend implementation compatible with [goodfirstissues.com](https://goodfirstissues.com/).

## About

This project explores Streamlit's potential as a general-purpose web frontend framework, beyond traditional data applications. It demonstrates how Streamlit can be used to build interactive web interfaces for browsing and filtering GitHub issues labeled as "good first issue" and so on.

## Deployment

The [deploy](https://github.com/zyfy29/goodfirstissues-streamlit/tree/deploy) branch is deployed in Streamlit Cloud https://goodfirstissues.streamlit.app/ by free.

## Development

We use st.secrets for managing secrets. Before running the app, create the `.streamlit/secrets.toml` file:

```toml
data_url = "https://raw.githubusercontent.com/darensin01/goodfirstissues/master/backend/data.json"
```

Then you can build and run it with Poetry.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to contribute to this project.
