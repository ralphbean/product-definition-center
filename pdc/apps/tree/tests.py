# -*- coding: utf-8 -*-
#
# Copyright (c) 2015 Red Hat
# Licensed under The MIT License (MIT)
# http://opensource.org/licenses/MIT
#
import json

from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase
from rest_framework import status

rpms_json = """{
    "header": {
        "version": "1.0"
    },
    "payload": {
        "compose": {
            "date": "20160531",
            "id": "shells-x86_64-20160531-458ed2b.0",
            "respin": 0,
            "type": "nightly"
        },
        "rpms": {
            "shells": {
                "x86_64": {
                    "aesh-0:0.33.7-4.fc24.src": {
                        "aesh-0:0.33.7-4.fc24.noarch": {
                            "category": "binary",
                            "path": "rpms/Packages/aesh-0.33.7-4.fc24.noarch.rpm",
                            "sigkey": null
                        },
                        "aesh-0:0.33.7-4.fc24.src": {
                            "category": "source",
                            "path": "source_rpms/Packages/aesh-0.33.7-4.fc24.src.rpm",
                            "sigkey": null
                        }
                    },
                    "copy-jdk-configs-0:1.1-4.fc24.src": {
                        "copy-jdk-configs-0:1.1-4.fc24.noarch": {
                            "category": "binary",
                            "path": "rpms/Packages/copy-jdk-configs-1.1-4.fc24.noarch.rpm",
                            "sigkey": null
                        },
                        "copy-jdk-configs-0:1.1-4.fc24.src": {
                            "category": "source",
                            "path": "source_rpms/Packages/copy-jdk-configs-1.1-4.fc24.src.rpm",
                            "sigkey": null
                        }
                    },
                    "dash-0:0.5.8-4.fc24.src": {
                        "dash-0:0.5.8-4.fc24.src": {
                            "category": "source",
                            "path": "source_rpms/Packages/dash-0.5.8-4.fc24.src.rpm",
                            "sigkey": null
                        },
                        "dash-0:0.5.8-4.fc24.x86_64": {
                            "category": "binary",
                            "path": "rpms/Packages/dash-0.5.8-4.fc24.x86_64.rpm",
                            "sigkey": null
                        }
                    },
                    "ed-0:1.12-2.fc24.src": {
                        "ed-0:1.12-2.fc24.src": {
                            "category": "source",
                            "path": "source_rpms/Packages/ed-1.12-2.fc24.src.rpm",
                            "sigkey": null
                        },
                        "ed-0:1.12-2.fc24.x86_64": {
                            "category": "binary",
                            "path": "rpms/Packages/ed-1.12-2.fc24.x86_64.rpm",
                            "sigkey": null
                        },
                        "ed-debuginfo-0:1.12-2.fc24.x86_64": {
                            "category": "debug",
                            "path": "debug_rpms/Packages/ed-debuginfo-1.12-2.fc24.x86_64.rpm",
                            "sigkey": null
                        }
                    },
                    "exim-0:4.86.2-1.fc24.src": {
                        "exim-0:4.86.2-1.fc24.src": {
                            "category": "source",
                            "path": "source_rpms/Packages/exim-4.86.2-1.fc24.src.rpm",
                            "sigkey": null
                        },
                        "exim-0:4.86.2-1.fc24.x86_64": {
                            "category": "binary",
                            "path": "rpms/Packages/exim-4.86.2-1.fc24.x86_64.rpm",
                            "sigkey": null
                        },
                        "exim-debuginfo-0:4.86.2-1.fc24.x86_64": {
                            "category": "debug",
                            "path": "debug_rpms/Packages/exim-debuginfo-4.86.2-1.fc24.x86_64.rpm",
                            "sigkey": null
                        }
                    },
                    "fish-0:2.2.0-11.fc24.src": {
                        "fish-0:2.2.0-11.fc24.src": {
                            "category": "source",
                            "path": "source_rpms/Packages/fish-2.2.0-11.fc24.src.rpm",
                            "sigkey": null
                        },
                        "fish-0:2.2.0-11.fc24.x86_64": {
                            "category": "binary",
                            "path": "rpms/Packages/fish-2.2.0-11.fc24.x86_64.rpm",
                            "sigkey": null
                        }
                    },
                    "java-1.8.0-openjdk-0:1.8.0.72-13.b16.fc24.src": {
                        "java-1.8.0-openjdk-debuginfo-1:1.8.0.72-13.b16.fc24.x86_64": {
                            "category": "debug",
                            "path": "debug_rpms/Packages/java-1.8.0-openjdk-debuginfo-1.8.0.72-13.b16.fc24.x86_64.rpm",
                            "sigkey": null
                        },
                        "java-1.8.0-openjdk-headless-1:1.8.0.72-13.b16.fc24.x86_64": {
                            "category": "binary",
                            "path": "rpms/Packages/java-1.8.0-openjdk-headless-1.8.0.72-13.b16.fc24.x86_64.rpm",
                            "sigkey": null
                        }
                    },
                    "java-1.8.0-openjdk-1:1.8.0.72-13.b16.fc24.src": {
                        "java-1.8.0-openjdk-1:1.8.0.72-13.b16.fc24.src": {
                            "category": "source",
                            "path": "source_rpms/Packages/java-1.8.0-openjdk-1.8.0.72-13.b16.fc24.src.rpm",
                            "sigkey": null
                        }
                    },
                    "ksh-0:20120801-29.fc24.src": {
                        "ksh-0:20120801-29.fc24.src": {
                            "category": "source",
                            "path": "source_rpms/Packages/ksh-20120801-29.fc24.src.rpm",
                            "sigkey": null
                        },
                        "ksh-0:20120801-29.fc24.x86_64": {
                            "category": "binary",
                            "path": "rpms/Packages/ksh-20120801-29.fc24.x86_64.rpm",
                            "sigkey": null
                        }
                    },
                    "libXfont-0:1.5.1-4.fc24.src": {
                        "libXfont-0:1.5.1-4.fc24.src": {
                            "category": "source",
                            "path": "source_rpms/Packages/libXfont-1.5.1-4.fc24.src.rpm",
                            "sigkey": null
                        },
                        "libXfont-0:1.5.1-4.fc24.x86_64": {
                            "category": "binary",
                            "path": "rpms/Packages/libXfont-1.5.1-4.fc24.x86_64.rpm",
                            "sigkey": null
                        },
                        "libXfont-debuginfo-0:1.5.1-4.fc24.x86_64": {
                            "category": "debug",
                            "path": "debug_rpms/Packages/libXfont-debuginfo-1.5.1-4.fc24.x86_64.rpm",
                            "sigkey": null
                        }
                    },
                    "libfontenc-0:1.1.3-3.fc24.src": {
                        "libfontenc-0:1.1.3-3.fc24.src": {
                            "category": "source",
                            "path": "source_rpms/Packages/libfontenc-1.1.3-3.fc24.src.rpm",
                            "sigkey": null
                        },
                        "libfontenc-0:1.1.3-3.fc24.x86_64": {
                            "category": "binary",
                            "path": "rpms/Packages/libfontenc-1.1.3-3.fc24.x86_64.rpm",
                            "sigkey": null
                        },
                        "libfontenc-debuginfo-0:1.1.3-3.fc24.x86_64": {
                            "category": "debug",
                            "path": "debug_rpms/Packages/libfontenc-debuginfo-1.1.3-3.fc24.x86_64.rpm",
                            "sigkey": null
                        }
                    },
                    "libgsasl-0:1.8.0-8.fc24.src": {
                        "libgsasl-0:1.8.0-8.fc24.src": {
                            "category": "source",
                            "path": "source_rpms/Packages/libgsasl-1.8.0-8.fc24.src.rpm",
                            "sigkey": null
                        },
                        "libgsasl-0:1.8.0-8.fc24.x86_64": {
                            "category": "binary",
                            "path": "rpms/Packages/libgsasl-1.8.0-8.fc24.x86_64.rpm",
                            "sigkey": null
                        },
                        "libgsasl-debuginfo-0:1.8.0-8.fc24.x86_64": {
                            "category": "debug",
                            "path": "debug_rpms/Packages/libgsasl-debuginfo-1.8.0-8.fc24.x86_64.rpm",
                            "sigkey": null
                        }
                    },
                    "libntlm-0:1.4-5.fc24.src": {
                        "libntlm-0:1.4-5.fc24.src": {
                            "category": "source",
                            "path": "source_rpms/Packages/libntlm-1.4-5.fc24.src.rpm",
                            "sigkey": null
                        },
                        "libntlm-0:1.4-5.fc24.x86_64": {
                            "category": "binary",
                            "path": "rpms/Packages/libntlm-1.4-5.fc24.x86_64.rpm",
                            "sigkey": null
                        },
                        "libntlm-debuginfo-0:1.4-5.fc24.x86_64": {
                            "category": "debug",
                            "path": "debug_rpms/Packages/libntlm-debuginfo-1.4-5.fc24.x86_64.rpm",
                            "sigkey": null
                        }
                    },
                    "lksctp-tools-0:1.0.16-5.fc24.src": {
                        "lksctp-tools-0:1.0.16-5.fc24.src": {
                            "category": "source",
                            "path": "source_rpms/Packages/lksctp-tools-1.0.16-5.fc24.src.rpm",
                            "sigkey": null
                        },
                        "lksctp-tools-0:1.0.16-5.fc24.x86_64": {
                            "category": "binary",
                            "path": "rpms/Packages/lksctp-tools-1.0.16-5.fc24.x86_64.rpm",
                            "sigkey": null
                        },
                        "lksctp-tools-debuginfo-0:1.0.16-5.fc24.x86_64": {
                            "category": "debug",
                            "path": "debug_rpms/Packages/lksctp-tools-debuginfo-1.0.16-5.fc24.x86_64.rpm",
                            "sigkey": null
                        }
                    },
                    "lua-posix-0:33.3.1-2.fc24.src": {
                        "lua-posix-0:33.3.1-2.fc24.src": {
                            "category": "source",
                            "path": "source_rpms/Packages/lua-posix-33.3.1-2.fc24.src.rpm",
                            "sigkey": null
                        },
                        "lua-posix-0:33.3.1-2.fc24.x86_64": {
                            "category": "binary",
                            "path": "rpms/Packages/lua-posix-33.3.1-2.fc24.x86_64.rpm",
                            "sigkey": null
                        },
                        "lua-posix-debuginfo-0:33.3.1-2.fc24.x86_64": {
                            "category": "debug",
                            "path": "debug_rpms/Packages/lua-posix-debuginfo-33.3.1-2.fc24.x86_64.rpm",
                            "sigkey": null
                        }
                    },
                    "mksh-0:52c-1.fc24.src": {
                        "mksh-0:52c-1.fc24.src": {
                            "category": "source",
                            "path": "source_rpms/Packages/mksh-52c-1.fc24.src.rpm",
                            "sigkey": null
                        },
                        "mksh-0:52c-1.fc24.x86_64": {
                            "category": "binary",
                            "path": "rpms/Packages/mksh-52c-1.fc24.x86_64.rpm",
                            "sigkey": null
                        }
                    },
                    "mosh-0:1.2.5-3.fc24.src": {
                        "mosh-0:1.2.5-3.fc24.src": {
                            "category": "source",
                            "path": "source_rpms/Packages/mosh-1.2.5-3.fc24.src.rpm",
                            "sigkey": null
                        },
                        "mosh-0:1.2.5-3.fc24.x86_64": {
                            "category": "binary",
                            "path": "rpms/Packages/mosh-1.2.5-3.fc24.x86_64.rpm",
                            "sigkey": null
                        }
                    },
                    "tcsh-0:6.19.00-4.fc24.src": {
                        "tcsh-0:6.19.00-4.fc24.src": {
                            "category": "source",
                            "path": "source_rpms/Packages/tcsh-6.19.00-4.fc24.src.rpm",
                            "sigkey": null
                        },
                        "tcsh-0:6.19.00-4.fc24.x86_64": {
                            "category": "binary",
                            "path": "rpms/Packages/tcsh-6.19.00-4.fc24.x86_64.rpm",
                            "sigkey": null
                        }
                    },
                    "tzdata-0:2016a-1.fc24.src": {
                        "tzdata-java-0:2016a-1.fc24.noarch": {
                            "category": "binary",
                            "path": "rpms/Packages/tzdata-java-2016a-1.fc24.noarch.rpm",
                            "sigkey": null
                        }
                    },
                    "xorg-x11-font-utils-0:7.5-31.fc24.src": {
                        "xorg-x11-font-utils-1:7.5-31.fc24.x86_64": {
                            "category": "binary",
                            "path": "rpms/Packages/xorg-x11-font-utils-7.5-31.fc24.x86_64.rpm",
                            "sigkey": null
                        },
                        "xorg-x11-font-utils-debuginfo-1:7.5-31.fc24.x86_64": {
                            "category": "debug",
                            "path": "debug_rpms/Packages/xorg-x11-font-utils-debuginfo-7.5-31.fc24.x86_64.rpm",
                            "sigkey": null
                        }
                    },
                    "xorg-x11-font-utils-1:7.5-31.fc24.src": {
                        "xorg-x11-font-utils-1:7.5-31.fc24.src": {
                            "category": "source",
                            "path": "source_rpms/Packages/xorg-x11-font-utils-7.5-31.fc24.src.rpm",
                            "sigkey": null
                        }
                    },
                    "yash-0:2.41-1.fc24.src": {
                        "yash-0:2.41-1.fc24.src": {
                            "category": "source",
                            "path": "source_rpms/Packages/yash-2.41-1.fc24.src.rpm",
                            "sigkey": null
                        },
                        "yash-0:2.41-1.fc24.x86_64": {
                            "category": "binary",
                            "path": "rpms/Packages/yash-2.41-1.fc24.x86_64.rpm",
                            "sigkey": null
                        }
                    },
                    "zsh-0:5.2-5.fc24.src": {
                        "zsh-0:5.2-5.fc24.src": {
                            "category": "source",
                            "path": "source_rpms/Packages/zsh-5.2-5.fc24.src.rpm",
                            "sigkey": null
                        },
                        "zsh-0:5.2-5.fc24.x86_64": {
                            "category": "binary",
                            "path": "rpms/Packages/zsh-5.2-5.fc24.x86_64.rpm",
                            "sigkey": null
                        }
                    },
                    "zvbi-0:0.2.35-1.fc24.src": {
                        "zvbi-0:0.2.35-1.fc24.src": {
                            "category": "source",
                            "path": "source_rpms/Packages/zvbi-0.2.35-1.fc24.src.rpm",
                            "sigkey": null
                        },
                        "zvbi-fonts-0:0.2.35-1.fc24.noarch": {
                            "category": "binary",
                            "path": "rpms/Packages/zvbi-fonts-0.2.35-1.fc24.noarch.rpm",
                            "sigkey": null
                        }
                    }
                }
            }
        }
    }
}"""

class TreeAPITestCase(APITestCase):
    def test_create_treevariant(self):
        url = reverse('treevariant-list')
        data = { 'variant_id': "core", 'variant_uid': "Core", 'variant_name': "Core", 'variant_version': "0-1", 'variant_type': 'module'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_tree(self):
        url = reverse('treevariant-list')
        data = { 'variant_id': "shells", 'variant_uid': "Shells", 'variant_name': "Shells", 'variant_version': "0-1", 'variant_type': 'module'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        url = reverse('tree-list')
        data = { 'tree_id': "Shells-x86_64-20160529.0", 'tree_date': "2016-05-29", 'variant': {"variant_uid": "Shells", "variant_version": "0-1"}, 'arch': "x86_64", 'content_format': ['rpm',], 'content': {'rpm' : json.dumps(json.loads(rpms_json))}, 'url': "/mnt/test/location"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
