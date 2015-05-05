# WARNING: Do not edit by hand, this file was generated by Crank:
#
#   https://github.com/gocardless/crank
#

import os
import re
import json

import responses

import gocardless_pro

def load_fixture(resource):
    fixtures_path = os.path.join(os.path.dirname(__file__), 'fixtures')
    fixture_filename = '{0}.json'.format(resource)
    fixture_path = os.path.join(fixtures_path, fixture_filename)
    return json.load(open(fixture_path))

def stub_response(resource_fixture):
    path = re.sub(r':(\w+)', r'\w+', resource_fixture['path_template'])
    url_pattern = re.compile('http://example.com' + path)
    json_body = json.dumps(resource_fixture['body'])
    responses.add(resource_fixture['method'], url_pattern, body=json_body)

client = gocardless_pro.Client(access_token='secret', base_url='http://example.com')
