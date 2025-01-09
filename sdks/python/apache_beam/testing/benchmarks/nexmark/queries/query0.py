#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

"""Nexmark Query 0: Pass through (send and receive auction events).

The Nexmark suite is a series of queries (streaming pipelines) performed
on a simulation of auction events.

This query is a pass through that
simply parses the events generated by the launcher. It serves as a test
to verify the infrastructure.
"""

# pytype: skip-file

import apache_beam as beam


class RoundTripFn(beam.DoFn):

  def process(self, element):
    coder = element.CODER
    byte_value = coder.encode(element)
    recon = coder.decode(byte_value)
    yield recon


def load(events, metadata=None, pipeline_options=None):
  return (
      events
      | 'serialization_and_deserialization' >> beam.ParDo(RoundTripFn()))
