# Contributing to hutch

## Bug reports and feature requests

Bug reports and feature requests are very welcome! Please create them as [issues](https://github.com/cariad/hutch/issues).

Issues written with AI assistance are welcome.

## Code changes

If you want to contribute a code change, please find or create the [issue](https://github.com/cariad/hutch/issues) first, then leave a comment to mention [@cariad](https://github.com/cariad) to let me know you want to take it on. Wait until we've discussed and agreed the change before submitting a pull request.

**Unplanned and unexpected pull requests won't be accepted.**

Code written with AI assistance is welcome.

## Development prerequisites

- [mise](https://mise.jdx.dev/)

## Getting started

Clone the repository, trust its mise configuration, and install the tools:

```bash
git clone https://github.com/cariad/hutch.git
cd hutch
mise trust
mise install
```

Run your local copy of the command line tool:

```bash
uv run hutch
```

## Linting

```bash
mise run lint
```

Many problems can be fixed automatically:

```bash
mise run fix
```

## Testing

```bash
mise run test
```
