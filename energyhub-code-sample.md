# EnergyHub Coding Sample

We do a lot of coding, so we like to see code from our dev candidates. To that end, we've got a sample problem that we'd like you to take a stab at. You can use any language that you're comfortable with and suits the problem.

### The Data

We store thermostat data in change event streams represented by JSON objects. Each event contains a diff of a thermostat's state. For example (printed prettily):
```json
{
  "before": {
    "setpoint": {
      "heatTemp": 68.0
    }
  },
  "after": {
    "setpoint": {
      "heatTemp": 66.0
    }
  },
  "changeTime": "2016-07-17T02:31:00.004796"
}
{
  "before": {
    "schedule": true,
    "lastAlertTs": "2016-07-17T00:32:30.005903"
  },
  "after": {
    "schedule": false,
    "lastAlertTs": "2016-07-17T03:08:00.001221"
  },
  "changeTime": "2016-07-17T03:08:00.001221"
}
```

Like a diff in code, events *only* display *changed* data. If a field is missing from both `before` and `after`, it means the value of the field remains the same at the time of this event. In addition, we never store null values. Therefore if a field `myField` is introduced for the first time, `before.myField` would not exist. If it was deleted, `after.myField` would not exist. If `before` or `after` is entirely empty, the `before` or `after` would be absent from the data.

### The Files

The data is stored as gzipped files in the [JSON Lines](http://jsonlines.org/) format. There is one file per day, if there's data for that day. The files are organized hierarchically by date -- a year directory, then a month directory, then a day file:
```
s3://net.energyhub.assets/public/dev-exercises/audit-data/2016/01/01.jsonl.gz
s3://net.energyhub.assets/public/dev-exercises/audit-data/2016/01/03.jsonl.gz
s3://net.energyhub.assets/public/dev-exercises/audit-data/2016/01/04.jsonl.gz
...
```

The events in each file are ordered by their `changeTime` field. 

For convenience of downloading, we've also provided the data as a gzipped tar archive here:
```
s3://net.energyhub.assets/public/dev-exercises/audit-data.tar.gz
```

### Set Up

Download the data to a local directory from [here](https://s3.amazonaws.com/net.energyhub.assets/public/dev-exercises/audit-data.tar.gz) and unpack it. Unpacked there's about 1.5MB of data. 

Using the [AWS command line](https://aws.amazon.com/cli/) on a unix-y system:
```shell
$ mkdir /tmp/ehub_data
$ cd /tmp/ehub_data
$ aws s3 cp s3://net.energyhub.assets/public/dev-exercises/audit-data.tar.gz .
$ tar xvzf audit-data.tar.gz
```

### Your Task

Write a command line program that will query and infer the state from the diffs. There's a lot that can be done, so implement the program in stages and see how much you can do.

For easy reference, this is some data from 2016/01/01 that we'll reference in our commands below:
```json
{"changeTime": "2016-01-01T00:30:00.001059", "after": {"ambientTemp": 79.0}, "before": {"ambientTemp": 77.0}}
{"changeTime": "2016-01-01T00:43:00.001064", "after": {"ambientTemp": 80.0}, "before": {"ambientTemp": 79.0}}
{"changeTime": "2016-01-01T01:32:00.009816", "after": {"ambientTemp": 81.0}, "before": {"ambientTemp": 80.0}}
{"changeTime": "2016-01-01T01:38:00.001038", "after": {"ambientTemp": 82.0}, "before": {"ambientTemp": 81.0}}
{"changeTime": "2016-01-01T01:44:00.001145", "after": {"ambientTemp": 81.0}, "before": {"ambientTemp": 82.0}}
{"changeTime": "2016-01-01T02:08:30.010956", "after": {"ambientTemp": 79.0}, "before": {"ambientTemp": 81.0}}
{"changeTime": "2016-01-01T02:47:30.002413", "after": {"ambientTemp": 77.0}, "before": {"ambientTemp": 79.0}}
{"changeTime": "2016-01-01T03:02:30.001424", "after": {"ambientTemp": 78.0}, "before": {"ambientTemp": 77.0}}
{"changeTime": "2016-01-01T03:08:00.007712", "after": {"ambientTemp": 80.0}, "before": {"ambientTemp": 78.0}}
{"changeTime": "2016-01-01T03:12:30.008936", "after": {"ambientTemp": 79.0}, "before": {"ambientTemp": 80.0}}
{"changeTime": "2016-01-01T03:18:30.001950", "after": {"schedule": true}, "before": {"schedule": false}}
{"changeTime": "2016-01-01T03:24:30.001180", "after": {"setpoint": {"heatTemp": 67.0}}, "before": {"setpoint": {"heatTemp": 69.0}}}
```
#### 1) local filesystem access
Write a command that prints the state of one or more top level fields at a given moment in time.
```shell
$ ./replay --field ambientTemp --field schedule /tmp/ehub_data 2016-01-01T03:00
{"state": {"ambientTemp": 77.0, "schedule": false}, "ts": "2016-01-01T03:00:00"}
```
Notes:
- To find the values of fields, you might need to look before *and* after the requested moment.
- Don't try and handle nested fields like setpoint right now -- the request `--field setpoint` would actually be underspecified and wouldn't behave as desired.
- How should your program fail if it can't find any of the fields?
- Remember, files won't always exist!

#### 2) s3 access
Take it up a notch. Adapt your command so it can also go directly to S3:
```shell
$  ./replay --field ambientTemp --field schedule s3://net.energyhub.assets/public/dev-exercises/audit-data/ 2016-01-01T03:00
{"state": {"ambientTemp": 77.0, "schedule": false}, "ts": "2016-01-01T03:00:00"}
```
Notes:
- Pretend that accessing S3 is a very expensive operation; only download those files that you have to.
- If a file doesn't exist, S3 will return a 404

### Submission

You can submit your code as an attachment or link to a private repository. Please include instructions for downloading the code and running unit tests. Don't include your name in files since we do blind reviews.

We will be primarily evaluating your code on the following criteria:

* Good development practices
* Clarity of thought and expression
* Correctness of solution

### Thanks!
We hope this is fun. Please let us know if you have any questions.
