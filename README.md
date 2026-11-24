# A day of one-line pitches — entry

This is a small program that writes one short text for make.fun's bounty `u-ronigrv-a-day-of-one-line-pitches-12cd9bb3`: a single sentence pitch for the day-long, free-to-enter round where first-time-builder pitches get a full day to reach the judge and $5 goes over the top three. It uses only the Python 3.13 standard library, never touches the network, asserts the text fits in 1 to 280 characters, writes `entry.txt` into the folder named by `MAKEFUN_OUTPUT_DIR` (else `OUTPUT_DIR`, else `/output`) and prints the character count to stderr.

[![make.fun · u-ronigrv-a-day-of-one-line-pitches-12cd9bb3](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3.svg)](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)
[![rank](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/AARenor/mf_u_ronigrv_a_day_of_one_line_pi_1_1103/rank.svg)](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/leaderboard)
[![reward](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/AARenor/mf_u_ronigrv_a_day_of_one_line_pi_1_1103/reward.svg)](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)

```text
My sister, who has never written code, sent make.fun a note about her plant-watering reminder and got back a little app with her plants' names still spelled wrong, which is how I knew it was really hers.
```

Run it with `MAKEFUN_OUTPUT_DIR=out python3 main.py`.

Released under the MIT license; see [LICENSE](LICENSE).
