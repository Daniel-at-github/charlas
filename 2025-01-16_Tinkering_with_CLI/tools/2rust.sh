#!/usr/bin/env bash
# Construct a slide for a command

title="$1"
command="$2"

rm -f command_output
(
    export PS1=""
    script --quiet --command "$command" command_output
)
echo "
== $title

// Description

#terminal([
  \`\`\`sh
  $command
  \`\`\`
  #render(\"
"
# Transform ansi codes to rust format
sed -e 's/\x1b/\\u{1b}/g' -e 's/"/\\"/g' < command_output
echo "
\")
])
"
