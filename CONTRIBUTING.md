# Contributing to GigaBookLM

> This is supposed to be a highly-lightweight and all-local project, so there are non-negotiable things to consider. In order for your fork to be accepted, these rules have to be followed to the letter.

## Non-Negotiable Rules to Consider
1. **RAM Crisis Factor:** All code must be optimized for low-memory environments.
2. **Air-Gapped by Design**: If your code touches the internet for unnecessary reasons, it’s a security breach. We don't phone home. Ever. But, if it does for 
3. **Memory is a Luxury**: We are solving the 2026 RAM Crisis. If your PR spikes memory usage without a massive performance gain, it's not accepted.
4. **Logic over Bloat:** If a 50-line Python script can do what a 2GB library does, you are most welcome!

## Workflow
> NOTE: Check if the feature you're thinking of, has been already implemented, by checking it through in the *Issues* tab.

1. **Fork and PR:** We do not grant direct push access. Submit your logic for audit. And, it will take time for auditing, so be patient.
2. **One Feature per PR:** One feature per PR. Do not send us a "code refactor" that hides a backdoor, with lots of lines.
3. **Documentation:** If you add a function, explain the logic. We don't do "Trust me, bro" code. And, no hate on **vibe-coding**, but this needs _a human touch_, and _a manual verification_. But, if you can't explain it properly, only then you can use AI.

## Standards to Follow
1. **Strings:** 'Single quotes' only.
2. **Naming:** logic_focused_naming, no temp1, temp2.
3. **Dependencies:** Every new import is a potential liability. Justify it.

By the way, if i didn't follow the mentioned rules here, feel free to point out.
