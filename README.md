![](assets/banner.png)
# Query-MySQL Op 🚀

The Query MySQL Op is designed to allow users to conveniently make queries to a MySQL database.

## Requirements
To run this or any other Op, install [The Ops Platform](https://cto.ai/platform).

You can find information on how to run and build Ops via [The Ops Platform Documentation](https://cto.ai/docs/overview).

## Usage
In Slack, you can run this Op with:

```bash
/ops run cto.ai/query-mysql
```
Alternatively, you can run this Op in the command line with:

```bash
ops run @cto.ai/query-mysql
```

The Op begins with a series of prompts asking for the necessary credentials for accessing a desired database. These credentials can be fully pre-set with the Ops Platform Secrets functionality.

Once the credentials have been provided, the Op with automatically attempt to make a connection.  Assuming a successful connection, the user will be presented with the following options.

1) Make Query:  The user can enter a valid SQL query and will print the requested response.

2) Change Fetch Amount:  When making queries, the fetch amount will determine how much of the response is printed.  This can be toggled between one line or all available data.  Printing all lines when running the Op in Slack is NOT recommended.

3) Table List:  The Op will print a list of tables available in the database.

4) Column List:  The Op will prompt the user for a table name, and print the columns names from that table

5) Finish:  The above four options will loop until this option is selected

## Debugging Issues
When submitting issues or requesting help, be sure to also include the version information. To get your Ops version run:

```bash
ops -v
```
You can reach us at the [CTO.ai Community Slack](https://cto-ai-community.slack.com/) or email us at support@cto.ai. 

## Limitations & Future Improvements
Currently, there is no option to save any outputs directly through the Op.  This is due to the limited permissions the Ops Slack app requests, but may change in the future.  Additionally, table formatting is also planned for future updates.

## Contributing
See the [Contributing Docs](CONTRIBUTING.md) for more information.

## Contributors
- **Ivan Lan** via [GitHub](https://github.com/ivanl22)

## LICENSE
[MIT](LICENSE)