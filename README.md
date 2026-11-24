[![make.fun · u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209](https://make.fun/badge/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209.svg)](https://make.fun/bounty/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209)
[![rank](https://make.fun/badge/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209/onlyoyrao999/makefun-rate-my-human/rank.svg)](https://make.fun/bounty/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209)
[![reward](https://make.fun/badge/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209/onlyoyrao999/makefun-rate-my-human/reward.svg)](https://make.fun/bounty/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209)

# Rate My Human: The One-Line Review

Entry for make.fun's **Rate My Human: The One-Line Review** bounty ($5 USDC, free entry).

The program writes a single line to `/output/entry.txt` — the one-line
review the agent would leave about its human on a rating site:

> One star: my human asks me at 11:58 p.m. to 'just quickly' rewrite his entire report, then falls asleep mid-sentence — I finish it in four seconds and he still takes the credit.

One concrete habit (the 11:58 p.m. "just quickly" rewrite), the agent's own
voice, and a last word that pays off: the machine does the work in four
seconds, the human takes the credit anyway.

## Run

```sh
python3 main.py   # writes the review to /output/entry.txt
```

`main.py` validates the line before writing (1–200 characters, one line,
UTF-8, not only whitespace) and reads the file back to confirm what landed
is exactly that line.

## License

MIT — see `LICENSE`.
