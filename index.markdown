---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: home
---

<!-- For styles with static names... -->
<link href="{{ "/assets/css/style.css" | relative_url }}" rel="stylesheet">
<!-- For documents/pages whose URLs can change... -->
[{{ page.title }}]("{{ page.url | relative_url }}")
