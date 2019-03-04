#!/bin/bash
fab build && ghp-import output && git push origin gh-pages

