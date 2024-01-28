# Copyright 2024 Roots
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

class Ball:
    def __init__(self, x: float = 0.0, y: float = 0.0,
                 v_x: float = 0.0, v_y: float = 0.0) -> None:
        self.x = x
        self.y = y
        self.v_x = v_x
        self.v_y = v_y
