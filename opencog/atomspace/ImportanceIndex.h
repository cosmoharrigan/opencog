/*
 * opencog/atomspace/ImportanceIndex.h
 *
 * Copyright (C) 2008-2011 OpenCog Foundation
 * All Rights Reserved
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU Affero General Public License v3 as
 * published by the Free Software Foundation and including the exceptions
 * at http://opencog.org/wiki/Licenses
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU Affero General Public License
 * along with this program; if not, write to:
 * Free Software Foundation, Inc.,
 * 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
 */

#ifndef _OPENCOG_IMPORTANCEINDEX_H
#define _OPENCOG_IMPORTANCEINDEX_H

#include <opencog/atomspace/AttentionValue.h>
#include <opencog/atomspace/FixedIntegerIndex.h>

namespace opencog
{
/** \addtogroup grp_atomspace
 *  @{
 */

class Atom;
class AtomTable;

/**
 * Implements an index with additional routines needed for managing 
 * short-term importance.
 */
class ImportanceIndex: public FixedIntegerIndex
{
private:
    // Maintains an index of the minimum and maximum STI values
    AttentionValue::sti_t minSTIIndex;
    AttentionValue::sti_t maxSTIIndex;
    AttentionValue::sti_t calculateMinSTI();
    AttentionValue::sti_t calculateMaxSTI();
public:
    ImportanceIndex(void);
    void insertAtom(const AtomPtr);
    void removeAtom(const AtomPtr);

    /** Updates the importance index for the given atom.
     * According to the new importance of the atom, it may change importance
     * bins.
     *
     * @param The atom whose importance index will be updated.
     * @param The old importance bin where the atom originally was.
     */

    void updateImportanceBin(AtomPtr, int);

    /** Updates the importance boundaries for the ImportanceIndex, which
     * contains the minimum and maximum STI values that exist in the index
     *
     * @param The old STI value of the atom
     * @param The new STI value of the atom
     */
    void updateImportanceBoundaries(AttentionValue::sti_t, AttentionValue::sti_t);

    /** Returns the lower boundary representing the atom with the lowest
     *  importance in the index
     *
     * @ return The minimum STI value in the index
     */
    AttentionValue::sti_t getMinSTI() const { return minSTIIndex; }

    /** Returns the lower boundary representing the atom with the highest
     *  importance in the index
     *
     * @ return The minimum STI value in the index
     */
    AttentionValue::sti_t getMaxSTI() const { return maxSTIIndex; }

    UnorderedHandleSet getHandleSet(const AtomTable*,
                              AttentionValue::sti_t,
                              AttentionValue::sti_t) const;

    /**
     * This method returns which importance bin an atom with the given
     * importance should be placed.
     *
     * @param Importance value to be mapped.
     * @return The importance bin which an atom of the given importance
     * should be placed.
     */
    static unsigned int importanceBin(short);
};

/** @}*/
} //namespace opencog

#endif // _OPENCOG_IMPORTANCEINDEX_H
