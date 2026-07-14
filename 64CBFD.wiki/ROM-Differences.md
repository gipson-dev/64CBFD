There are 4 Conker ROMs in the wild, in reverse order of build date:

- `eu`; Jan 31 2001 13:29:42
- `us`; Dec 19 2000 09:57:42
- `debug`; Oct 25 2000 22:45:59
- `ects`; Aug 25 2000 15:45:59

The `eu`, `us` and `debug` versions are similar in terms of ROM layout - with game code being compressed. The game code is not compressed in the `ects` ROM.

## Compressed section

### File sizes

| name       | `us`      | `eu`      | `debug`   | `ects`    |
|:----------:|:---------:|:---------:|:---------:|:---------:|
| compressed | `9494881` | `9496318` | `9576797` | `9671887` |

### Number of compressed files

| name       | `us`   | `eu`   | `debug` | `ects` |
|:----------:|:------:|:------:|:-------:|:------:|
| compressed | `7760` | `7762` | `7808`  | `8427` |

## Assets

| name     | `us` size | `eu` size | `us == eu`? | `debug` size | `debug == us`? | `ects` size | `ects == debug` |
|:--------:|----------:|----------:|:-----------:|:------------:|:--------------:|:-----------:|:---------------:|
| assets00 | 274136    | 274136    | 🟢          | 286312       | 🔴            | 6240        |                 |
| assets01 | 774792    | 774768    | 🔴          | 785064       | 🔴            | 286312      | 🟡              |
| assets02 | 4052696   | 4052696   | 🟢          | 4058736      | 🔴            | 790520      |                 |
| assets03 | 62440     | 62472     | 🔴          | 66832        | 🔴            | 3311648     |                 |
| assets04 | 1793096   | 1793104   | 🔴          | 1784672      | 🔴            | 59936       |                 |
| assets05 | 179112    | 179008    | 🔴          | 176744       | 🔴            | 1881744     |                 |
| assets06 | 542048    | 542024    | 🔴          | 538480       | 🔴            | 173288      |                 |
| assets07 | 80        | 80        | 🟢          | 80           | 🔴            | 758048      |                 |
| assets08 | 896       | 896       | 🟢          | 896          | 🔴            | 80          |                 |
| assets09 | 362320    | 362312    | 🔴          | 361392       | 🔴            | 1992        |                 |
| assets0A | 268464    | 268464    | 🟢          | 268464       | 🔴            | 307008      |                 |
| assets0B | 11960     | 11960     | 🔴          | 11624        | 🔴            | 168760      |                 |
| assets0C | 251832    | 253320    | 🔴          | 231528       | 🔴            | 10472       |                 |
| assets0D | 456       | 456       | 🟢          | 456          | 🟢            | 195224      |                 |
| assets0E | 15680     | 15680     | 🔴          | 15528        | 🔴            | 304         |                 |
| assets0F | 78408     | 78408     | 🔴          | 284760       | 🔴            | 13760       |                 |
| assets10 | 23984     | 23984     | 🟢          | 23872        | 🔴            | 246480      |                 |
| assets11 | 14432     | 14432     | 🟢          | 14424        | 🔴            | 20088       |                 |
| assets12 | 3128      | 3128      | 🟢          | 3128         | 🔴            | 14080       |                 |
| assets13 | 19832     | 19832     | 🟢          | 19832        | 🟢            | 2816        |                 |
| assets14 | 169880    | 170128    | 🔴          | 163096       | 🔴            | 19832       | 🟡              |
| assets15 | 7648      | 7648      | 🟢          | 7632         | 🔴            | 154608      |                 |
| assets16 | 23586160  | 23586160  | 🟢          | 23677712     | 🔴            | 7816        |                 |
| assets17 | 22886280  | 22886280  | 🟢          | 22721648     | 🔴            | 19561184    |                 |
| assets18 | 800       | 800       | 🟢          | 4392         | 🟡            | 19908248    |                 |
| assets19 | 5848      | 5848      | 🟢          | 800          | 🔴            | 4392        | 🟡              |
| assets1A | 23256     | 23256     | 🟢          | 22184        | 🔴            | 800         | 🟡              |
| assets1B | 5336      | 5336      | 🟢          | 5848         | 🟡            | 19616       |                 |
| assets1C | 3160      | 3160      | 🟢          | 5336         | 🔴            | 5432        |                 |
| assets1D | 🇳🇦        | 🇳🇦        | 🇳🇦           | 🇳🇦           | 🇳🇦            | 5336        | 🟡              |
| assets1E | 🇳🇦        | 🇳🇦        | 🇳🇦           | 🇳🇦           | 🇳🇦            | 9272        |                 |

**Notes:**
- assets18/assets19 are swapped in the `debug` ROM, `assets18` matches across `us`, `eu` and `debug` ROMS.
- assets1B/assets1C are swapped in the `debug` ROM, `assets1B` matches across `us`, `eu` and `debug` ROMS.
- `ects` assets01 matches `debug` assets00 
- `ects` assets14 matches `debug` assets13
- `ects` assets19 matches `debug` assets18
- `ects` assets1A matches `debug` assets19
- `ects` assets1D matches `debug` assets1C
