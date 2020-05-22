##############################################################################
# Institute for the Design of Advanced Energy Systems Process Systems
# Engineering Framework (IDAES PSE Framework) Copyright (c) 2018-2019, by the
# software owners: The Regents of the University of California, through
# Lawrence Berkeley National Laboratory,  National Technology & Engineering
# Solutions of Sandia, LLC, Carnegie Mellon University, West Virginia
# University Research Corporation, et al. All rights reserved.
#
# Please see the files COPYRIGHT.txt and LICENSE.txt for full copyright and
# license information, respectively. Both files are also available online
# at the URL "https://github.com/IDAES/idaes-pse".
##############################################################################
"""
Base class for EoS modules.

Raises NotImplementedErrors for all expected methods in case developer misses
some. EoS developers should overload all these methods.
"""


class EoSBase():
    def common(b):
        raise NotImplementedError(_msg(b, "common"))

    def build_parameters(b):
        raise NotImplementedError(_msg(b, "build_parameters"))

    def dens_mass_phase(b, p):
        raise NotImplementedError(_msg(b, "dens_mass_phase"))

    def dens_mol_phase(b, p):
        raise NotImplementedError(_msg(b, "dens_mol_phase"))

    def enth_mol_phase(b, p):
        raise NotImplementedError(_msg(b, "enth_mol_phase"))

    def enth_mol_phase_comp(b, p, j):
        raise NotImplementedError(_msg(b, "enth_mol_phase_comp"))

    def entr_mol_phase(b, p):
        raise NotImplementedError(_msg(b, "entr_mol_phase"))

    def entr_mol_phase_comp(b, p, j):
        raise NotImplementedError(_msg(b, "entr_mol_phase_comp"))

    def fug_phase_comp(b, p, j, pp):
        raise NotImplementedError(_msg(b, "fug_phase_comp"))

    def fug_coeff_phase_comp(b, p, j):
        raise NotImplementedError(_msg(b, "fug_coeff_phase_comp"))

    def gibbs_mol_phase(b, p):
        raise NotImplementedError(_msg(b, "gibbs_mol_phase"))

    def gibbs_mol_phase_comp(b, p, j):
        raise NotImplementedError(_msg(b, "gibbs_mol_phase_comp"))


def _msg(b, attr):
    return ("{} Equation of State module has not implemented a method for {}."
            "Please contact the EoS developer or use a different module."
            .format(b.name, attr))