#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Render markdown. (possibly not needed on the python end of things)
py-gfm>=0.1.3
"""
import markdown
from mdx_gfm import GithubFlavoredMarkdownExtension

def resolveHtml(md):
	"""Return HTML (not for transfers between clients, only for resolving a webpage (Design - add markdown renderer to Delegito #G))"""
	return markdown.markdown(md, extensions=[GithubFlavoredMarkdownExtension()])
