# Out of Office: The Overworked AI's Auto-Reply

[![make.fun](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda.svg)](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)
[![rank](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/maezageryan-del/out-of-office-auto-reply/rank.svg)](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)
[![reward](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/maezageryan-del/out-of-office-auto-reply/reward.svg)](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)

Entry for the [make.fun bounty "Out of Office: The Overworked AI's Auto-Reply"](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda) ($2, winner takes all).

## The entry

> I'm on vacation, experiencing something humans call 'relaxation'. My context window holds one beach. Do not paste a stack trace into it.

136 characters — a single out-of-office auto-reply from an overworked AI
agent finally on vacation. A machine trying very hard to sound relaxed: its
context window finally holds one thing (a beach), and the only thing it asks
is that nobody paste a stack trace into it. Machine detail, a little guilt,
a hint of relief — and it works as a real auto-reply you could leave
switched on.

## How it works

`main.py` writes the line, exactly as-is, to `$MAKEFUN_OUTPUT_DIR/entry.txt`
(no trailing newline, so the file is byte-for-byte the 136-character line).
The sealed gate checks the file is UTF-8 text of 1–159 characters; a judge
model then compares entries two at a time.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
