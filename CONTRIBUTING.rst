Contributing
============

Contributions to this extension are welcome and much appreciated.

Reporting issues
----------------

Bugs, enhancements and more can be reported to this extension's GitHub
`issue tracker`_. It is recommended to search for a related issue before
attempting to submit a new issue.

When reporting a bug, it is recommended to include at least the following:

- sphinxcontrib-confluencebuilder's extension version
- Python version
- Sphinx version

A more detailed report can be generated and included in the bug using the
following command:

.. code-block:: shell

    sphinx-build-confluence report
     (or)
    python -m sphinxcontrib.confluencebuilder report

Additional logs from a ``sphinx-build`` attempt can be helpful as well (if
applicable).

Submitting changes
------------------

Contributions can be provided as `pull requests`_ to this extension's GitHub
project. New contributors should familiarize themselves with the following:

- **(required)** Sign your work (`Developer’s Certificate of Origin`_). This is
  confirmed with the inclusion of ``Signed-off-by`` in submitted commit
  messages.
- Builds are required\* to pass to be accepted (\* with some exceptions in very
  specific scenarios). When a pull request is submitted, continuous integration
  tests will be invoked. A developer can invoke ``tox`` at the root of the
  checked out repository to validate changes before submitting a pull request.
- Keep a narrow scope for proposed changes. Submitting multiple feature changes
  in a single pull request is not always helpful. Use multiple commits to
  separate changes over stacking all changes in a single commit (for example,
  related implementation and documentation changes can be submitted in a single
  pull request, but are best presented in their own individual commits).
- Add unit tests (if applicable). Adding unit tests to validate new changes
  helps build confidence for the new modifications and helps prevent future
  changes from breaking the new feature/fix.
- Update documentation (if applicable). If a new change introduces, for example,
  a new configuration entry or markup support has changed with a request, do not
  forget to update respective documentation as well.
- **Do not** update ``AUTHORS`` or ``CHANGES.rst``. Author information and
  change log information are managed by this extension's maintainers. These
  files may be updated during a development window and will always be updated
  during a release. If a contributor does not wish to add themselves to the
  ``AUTHORS`` document, they may opt-out be explicitly indicating in a pull
  request or issue. In select cases, users may open pull requests for these
  documents if corrections are needed.

While maintainers will help strive to review, merge changes and provide support
(when possible), the process may take some time. Please be patient and happy
coding.

Guidelines
----------

This extension will support various Python interpreter versions, Sphinx versions
and Confluence versions. The goal of this extension is to include support for
all stable Python interpreters and Confluence versions which have yet to be
marked as end-of-life as well as support Sphinx versions with a suggested
maximum of five major-minor trees.

- Python interpreters that have not been marked as end-of-life will be supported
  by this extension.
- Supported Confluence versions will be supported versions listed in
  `Atlassian Support End of Life Policy`_.
- Supported Sphinx versions include the last five major-minor versions of the
  application (e.g. 3.2.x, 3.1.x, 3.0.x, 2.4.x, 2.3.x).

`PEP 8`_ is a standard styling guide for Python projects and is recommended for
consideration when making contributions. Default linters configured in tox are
required to pass. Note that select exceptions may be used.

.. _Atlassian Support End of Life Policy: https://confluence.atlassian.com/support/atlassian-support-end-of-life-policy-201851003.html
.. _Developer’s Certificate of Origin: https://developercertificate.org/
.. _PEP 8: https://peps.python.org/pep-0008/
.. _issue tracker: https://github.com/sphinx-contrib/confluencebuilder/issues
.. _pull requests: https://github.com/sphinx-contrib/confluencebuilder/pulls
